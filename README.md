# CloudLevelManager
A Pythonic way to maintain and generate cloud levels for the EdgeProX and MotiveWave trading platforms.
- No need to cut and paste lines of CSV
- Control draw order
- Templating
- Automation

# The Basics
It's not a package -- just one file.  Place `CloudLevelManager.py` in your working path and import the module:
```python
from CloudLevelManager import CloudLevels
```
The most basic example -- we'll talk about the structure a little bit later:
```python
levels = {
    'support/resistance': [
        {'Price': 4309.50},
        {'Price': 4282.25},
        {'Price': 4249.50},
        ],
    }
# Create a CloudLevels object and write the CSV file
cl = CloudLevels('ES', levels, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
```
This will create three grey lines when loaded into EdgeProX/MotiveWave.  The top level key -- `'support/resistance'` in this case -- is the template name.
CloudLevelManager applied a built-in default template since we did not define one.

We can do better, and there are two ways to do that:
- With templates
- Explicitely for each level

## Templates
Templates define the default Cloud Level attributes for each style.  It is a nested dictionary with the top keys being the template name followed by key:value pairs of attributes such as the text label and band offset (or diameter).  CloudLevelManager has defaults for any attributes that you do not explicitely declare in your template.

Let's make a template:
```python
my_templates = {
    'support/resistance': {
        'Label': 'S/R Zone',
        'Text Color': '#FFFFFF', 'Line Color': '#800080', 'Band Color': '#800080',
        'Band Offset': 6,
        'Show Label': 'Y',
        'Show Price': 'Y',
        'Priority': 0,
        },
    'pivot': {
        'Label': 'Pivot',
        'Text Color': '#FFFFFF', 'Line Color': '#800080', 'Band Color': '#800080',
        'Band Offset': 6,
        'Show Label': 'Y',
        'Show Price': 'Y',
        'Priority': 0,
        },
}
```
CloudLevelManager requires a dictionary of templates.  Assuming you are familiar
with cloud levels, all those attributes should make sense except for...

'Priority': This attribute is an integer value used for graphical ordering.
Higher numbers print on top of lower numbers.

Now specify the template dict and you will have some nice purple s/r zones
```python
cl = CloudLevels('ES', levels, templates=my_templates, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
```
Let's use multiple templates in our levels
```python
levels = {
    'pivot': [
        {'Price': 4282.25},
        ],
    'support/resistance': [
        {'Price': 4309.50},
        {'Price': 4249.50},
        ],
    }
cl = CloudLevels('ES', levels, templates=my_templates, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
```
## Overrides
Now, the other way to control the attributes: Specify them in the levels dict.
Attributes specified in the levels dictionary take precedence over template settings.
```python
levels = {
    'pivot': [
        {'Price': 4282.25, 'Label': 'Central Pivot', 'Band Offset': 0},
        ],
    'support/resistance': [
        {'Price': 4309.50, 'Label': 'R1'},
        {'Price': 4249.50, 'Label': 'R2'},
        ],
    }

cl = CloudLevels('ES', levels, templates=my_templates, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
```
Now you should have the basics of templating and levels

## Price Ranges
CloudLevelManager will also accept price ranges and calculate the band offset for you.
Let's add to 'my_templates' and add some single prints as an example:
```python
my_templates['single print'] = {'Label': 'Single Print',
        'Text Color': '#FFFFFF', 'Line Color': '#FFAAE2', 'Band Color': '#FFAAE2',
        'Priority': -8,}
levels = {
    'single print': [
        {'Price Range': [4251.00, 4249.25]}, # order does not matter
        {'Price Range': [4240.00, 4243.50]}, # high/low or low/high
        {'Price Range': [4067.25, 4064.50]},
        ],
    }
cl = CloudLevels('ES', levels, templates=my_templates, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
```
Note that the 'tick_size' attribute is important here, as the band offset is in
ticks, not real numbers.  That limitation will also make some bands be off by
half a tick.  Nothing we can do about that.

## Multiple Dictionaries
So far, our levels have all been in a single `dict` object.  No problem if you manage your level groups separately -- you can hand CloudLevelManager a list of dicts:

```python
tech_levels = {
    'pivot': [
        {'Price': 4282.25, 'Label': 'Central Pivot', 'Band Offset': 0},
        ],
    'support/resistance': [
        {'Price': 4309.50, 'Label': 'R1'},
        {'Price': 4249.50, 'Label': 'R2'},
        ],
    }
tpo_levels = {
    'single print': [
        {'Price Range': [4251.00, 4249.25]}, # order does not matter
        {'Price Range': [4240.00, 4243.50]}, # high/low or low/high
        {'Price Range': [4067.25, 4064.50]},
        ],
    }
cl = CloudLevels('ES', [tech_levels, tpo_levels], templates=my_templates, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
```

## Next steps
Hopefully templating gives you a more flexible and manageable way to maintain
your cloud levels; but why stop there?  You can automate, or add some IO for
other file formats, or whatever.  Here's an idea to extend our support/resistance levels created above:
```python
levels['support/resistance'].extend([{'Price':i, 'Label': 'Century'} for i in range(3500, 5100, 100)])
```
There you go, all the century marks in one line of code!
