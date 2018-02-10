test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Difference_Growth18901914, 0.012)
          True
          """,
          'hidden': False,
          'locked': False
        },
        
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Difference_Growth19141946, 0.020)
          True
          """,
          'hidden': False,
          'locked': False
        },
      
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Difference_Growth19461980, 0.016)
          True
          """,
          'hidden': False,
          'locked': False
        },
    
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Difference_Growth19802992, 0.023)
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
