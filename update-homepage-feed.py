"""Run python update-homepage-feed.py after adding blog posts or podcast episodes."""
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parent
entries=[]
for folder,kind in [('blog/posts','Research Reflections'),('blogs/faith-lifestyle/posts','Faith & Lifestyle'),('blogs/leadership/posts','Leadership Reflections'),('podcast/episodes','Podcast')]:
    for file in (ROOT/folder).glob('*/index.qmd'):
        raw=file.read_text(encoding='utf-8')
        match=re.match(r'^---\s*\n(.*?)\n---',raw,re.S)
        if not match: continue
        front=match.group(1)
        def field(key):
            m=re.search(r'^'+re.escape(key)+r':\s*(.*)$',front,re.M)
            return m.group(1).strip().strip('\"\'') if m else ''
        if field('draft').lower()=='true' or field('published').lower()!='true': continue
        title=field('title')
        if not title: continue
        entries.append({'title':title,'type':kind,'description':field('description'),'date':field('date'),'url':file.relative_to(ROOT).with_suffix('.html').as_posix()})
script=(ROOT/'homepage-highlights.js')
existing=script.read_text(encoding='utf-8')
script.write_text(re.sub(r'const homepageItems = .*?;', 'const homepageItems = '+json.dumps(entries,ensure_ascii=False)+';',existing,count=1),encoding='utf-8')
print(f'Updated homepage with {len(entries)} published items.')
