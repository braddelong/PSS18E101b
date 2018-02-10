test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Y_when_s_doubles_pointninety, 512)
          True
          """,
          'hidden': False,
          'locked': False
        },

               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Y_when_s_doubles_pointseventyfive, 8)
          True
          """,
          'hidden': False,
          'locked': False
        },
    
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Y_when_s_doubles_pointsixty, 2.8)
          True
          """,
          'hidden': False,
          'locked': False
    
        },

               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Y_when_s_doubles_pointfortyfive, 1.8)
          True
          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Y_when_s_doubles_pointthirty, 1.35)
          True
          """,
          'hidden': False,
          'locked': False
        },
        
                {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Y_when_s_doubles_pointfifteen, 1.1)
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
