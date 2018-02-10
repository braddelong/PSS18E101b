test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Sweden_multiple18902015, 16.4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Argentinean_multiple18902015, 3.3)
          True
          """,
          'hidden': False,
          'locked': False
        },
      
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Quotient_multiple18902015, 4.9)
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
