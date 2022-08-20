# -*- coding: utf-8 -*-

#%% imports
import csv

#%% class
class CloudLevels:
    fieldnames = [
        'Symbol', 'Price', 'Label', 'Text Color', 'Line Color', 'Band Color',
        'Band Offset', 'Show Label', 'Show Price',
        ]
    default_template = {'Label': 'Misc', 'Text Color': '#FFFFFF', 'Line Color': '#808080', 'Band Color': '#808080', 
        'Band Offset': 0, 'Show Label': 'Y', 'Show Price': 'Y', 'Priority': 0,}


    def __init__(self, symbol, levels, templates={}, tick_size=0.01):
        _levels = levels.copy()
        # provide a default template
        self.level_dicts = []
        for k,v in _levels.items():
            template = templates.get(k, self.default_template) # use default if name missing
            #assign default values to any missing attributes
            for key in self.default_template.keys():
                template[key] = template.get(key, self.default_template[key])
            for level in v:
                level['Symbol'] = symbol
                for key in template.keys():
                    level[key] = level.get(key, template[key])
                # handle price ranges
                price_range = level.get('Price Range')
                if price_range:
                    level['Price'] = sum(price_range) / len(price_range)
                    level['Band Offset'] = (max(price_range) - min(price_range)) / (tick_size * 2)
                self.level_dicts.append(level)
        self.level_dicts.sort(key=lambda x: x['Priority'])
        if pd_query:
            pass
        
    def to_csv(self, filepath):
        rows = [{k: d[k] for k in d if k in self.fieldnames} for d in self.level_dicts]
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            
def range_bands_from_list(symbol, price_list, template1, template2, tick_size=0.01):
    bands = {1: template1, 2: template2}
    band = 1
    cl = {1:[], 2:[]}
    for i in range(len(price_list) - 1):
        cl[band].append({'Price Range': [price_list[i], price_list[i+1]] })
        if band == 1:
            band = 2
        else:
            band = 1

    return CloudLevels(symbol, cl, bands, tick_size)
