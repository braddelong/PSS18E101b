test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Growth_Rate_1000BC_to_1000AD, 0.0008, atol=0.001)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Growth_Rate_1400_to_1600, 0.0022, atol=0.001)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Growth_Rate_1900_to_1950, 0.0087, atol=0.001)
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
