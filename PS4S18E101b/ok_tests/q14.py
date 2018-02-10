test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KY_when_s_doubles_pointninety, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KY_when_s_doubles_pointseventyfive, 50)
          True
          """,
          'hidden': False,
          'locked': False
        },
      
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KY_when_s_doubles_pointsixty, 36)
          True
          """,
          'hidden': False,
          'locked': False
        },
    
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KY_when_s_doubles_pointfortyfive, 151)
          True
          """,
          'hidden': False,
          'locked': False
        }
    
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
