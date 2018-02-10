test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(YoverL45, 1.7)
          True
          """,
          'hidden': False,
          'locked': False
        },
        
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KoverL45, 14.1)
          True
          """,
          'hidden': False,
          'locked': False
        },
      
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(YoverL46, 3.2)
          True
          """,
          'hidden': False,
          'locked': False
        },
    
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KoverL46, 31.6)
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
