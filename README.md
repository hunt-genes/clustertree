# Clustertree

The brilliant Kanwei Li's clustertree algorithm. Extracted from bx-python to
make a dependency-free version. Thanks to James Taylor for the liberal license
on bx-python which enabled this standalone version!

## Maintainer

Endre Bakken Stovner

## Install

```
pip install clustertree
```

## Example

```
from clustertree import ClusterTree

c = ClusterTree(500, 3) # distance allowed, reads required.

c.insert(0, 1, 500) # start, end, id (int)

c.insert(0, 500, 1000)

c.getregions()
# []

c.insert(750, 1500, 1500)

c.getregions()
# [(0, 1500, [500, 1000, 1500])]
```

## License

MIT

## Read more

[Finding and displaying short reads clustered in the genome](https://bcbio.wordpress.com/2009/04/29/finding-and-displaying-short-reads-clustered-in-the-genome/)
