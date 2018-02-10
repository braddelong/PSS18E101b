test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(YoverL43, 2.4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KoverL43, 15)
          True
          """,
          'hidden': False,
          'locked': False
        },
      
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(YoverL44, 4)
          True
          """,
          'hidden': False,
          'locked': False
        },
    
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KoverL44, 35)
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
