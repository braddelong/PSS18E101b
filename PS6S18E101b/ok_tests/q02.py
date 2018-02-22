test = {
  'name': 'Problem Set 5 q02',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Output_per_worker2050, 468103, atol=1000)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Output_per_worker2100, 1055954, atol=1000)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(Output_per_worker2150, 2280114, atol=1000)
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
