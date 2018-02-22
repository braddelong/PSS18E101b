test = {
  'name': 'Problem Set 5 q02',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(KoverY_50_alphaquarter, 4.93, atol=0.01) 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(KoverY_50_alphathird, 4.90, atol=0.01)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(KoverY_50_alphahalf, 4.83, atol=0.01)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(KoverY_50_alphatwothirds, 4.69, atol=0.01)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(KoverY_50_alphathreequarters, 4.58, atol=0.1)
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
