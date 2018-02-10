test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(YoverL49, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },

               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KoverL49, 50)
          True
          """,
          'hidden': False,
          'locked': False
        },
               
               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KY_when_s_doubles_pointfifteen8, 36)
          True
          """,
          'hidden': False,
          'locked': False
        },

               {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KY_when_s_doubles_pointthirty, 151)
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
