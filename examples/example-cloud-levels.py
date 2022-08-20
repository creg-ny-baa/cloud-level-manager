#%% imports
from CloudLevelManager import CloudLevels
from CloudLevelTemplates import standard_templates
#%% variables
es_stats = {
    'stat': [ # default priority for stat is 10
        # --- prior day stats
        {'Label': 'pd-Open',    'Price': 4277.50},
        {'Label': 'pd-High',    'Price': 4295.50},
        {'Label': 'pd-Low',     'Price': 4264.00},
        {'Label': 'pd-Settle',  'Price': 4286.50},
        # --- overnight stats
        {'Label': 'on-High',    'Price': 4288.00},
        {'Label': 'on-Low',     'Price': 4241.00},
        # --- weekly stats
        {'Label': 'pw-Open',    'Price': 4149.75, 'Priority': 5},
        {'Label': 'pw-High',    'Price': 4282.75, 'Priority': 5},
        {'Label': 'pw-Low',     'Price': 4113.00, 'Priority': 5},
        {'Label': 'w-Open',     'Price': 4277.00, 'Priority': 5},
        {'Label': 'w-High',     'Price': 4327.50, 'Priority': 5},
        {'Label': 'w-Low',      'Price': 4249.00, 'Priority': 5},
    ],
}
# a one-liner to add century marks
es_stats['stat'].extend([{'Price':i, 'Label': 'Century', 'Priority': -5} for i in range(3500, 5100, 100)])
#%% support and resistance
es_sr = {
    's/r zone': [
        {'Price': 4303.50},
        {'Price': 4283.00},
        {'Price': 4264.00},
        {'Price': 4251.50},
        {'Price': 4220.00},
        {'Price': 4188.00},
        {'Price': 4161.00},
        {'Price': 4140.00},
        {'Price': 4112.50},
    ],
}
#%% market profile
es_market_profile = {
    # an example of ranges
    'lvn': [
        {'Price Range': [4283, 4241]},
        {'Price Range': [3879, 3867]},
        {'Price Range': [3849, 3836]},
        {'Price Range': [3807, 3798]},
    ],
    'vpoc': [
        {'Price': 4123.00,  'Label': 'pw-CVPOC'},
        {'Price': 3903.75,  'Label': 'Feb/Mar CVPOC'},
    ],
    'gap': [
        {'Price Range': [4178.50, 4138.75]},
        {'Price Range': [3819.75, 3800.00]},
    ],
    'hva': [
        {'Price Range': [3980, 3944], 'Label': '3w-HVA'}, # started 8 May
    ],
    'single print': [
        {'Price Range': [4251.00, 4249.25]},
        {'Price Range': [4243.50, 4240.00]},
        {'Price Range': [4067.25, 4064.50]},
        {'Price Range': [4063.00, 4058.25]},
    ],
    'poor extreme': [
        #{'Price': 4188.00, 'Label': 'Poor High'},
    ]
}
#%% technicals
es_technicals = {
    'technical': [
        {'Price': 4033.50, 'Label': '20d-SMA'},
    ],
}
#%% export support/resistance levels
cl_sr = CloudLevels('ES', es_sr, templates=standard_templates, tick_size=0.25)
cl_sr.to_csv('es-sr-levels.csv')
#%% export master levels
# this is a good example of why you should mange groups separately--
# becuase you can export individualy or roll them up like so:
es_master_levels = {**es_stats, **es_sr, **es_technicals}
cl_master = CloudLevels('ES', es_master_levels, templates=standard_templates, tick_size=0.25)
cl_master.to_csv('es-key-levels.csv')
#%% export market profile levels
cl_mp = CloudLevels('ES', es_market_profile, templates=standard_templates, tick_size=0.25)
cl_mp.to_csv('es-mktprof-levels.csv')
