from pathlib import Path

def read_quote(inpath):
    out = ''
    with inpath.open() as f:
        for line in f:
            if not line.startswith('#'):
                out += '> ' + line
    return out

tesla_quote = read_quote(Path('tesla-quote.md'))
haldane_quote = read_quote(Path('haldane-quote.md'))
musk_quote = read_quote(Path('musk-quote.md'))

raw = Path('post-raw.md').read_text()

with_quotes = raw.format(
        tesla_quote = tesla_quote,
        musk_quote = musk_quote,
        haldane_quote = haldane_quote
        )

outpath = Path('README.md')
outpath.write_text(with_quotes)
