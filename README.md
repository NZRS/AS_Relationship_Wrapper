# AS Relationship Wrapper

This code takes care of downloading, parsing and providing a high level interface to the AS Relationship [dataset](http://www.caida.org/data/as-relationships/) made available by [CAIDA](http://www.caida.org)

## Installation

```
python setup.py install
```

## Usage

```
import as_relationship.parser
import as_relationship.fetcher

new_file = as_relationship.fetcher.get_as_relationship_file(datadir='data')
s2 = as_relationship.parser.AsRelationship(rel_file=new_file)
```

