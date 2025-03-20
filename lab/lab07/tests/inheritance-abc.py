test = {
  'name': 'Inheritance ABCs',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...   x, y = 0, 0
          ...   def __init__(self):
          ...         return
          >>> class B(A):
          ...   def __init__(self):
          ...         return
          >>> class C(A):
          ...   def __init__(self):
          ...         return
          >>> print(A.x, B.x, C.x)
<<<<<<< HEAD
          0 0 0
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          0 2 0
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          1 2 1
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          False
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          1 1 1 1
          """,
          'hidden': False,
          'locked': False,
=======
          5dd1d444cfee04cb2069097fa040a660
          # locked
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          cfd0937eea29fcfd259be44001016aed
          # locked
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          49f2632a22ef174bac832e2a2ce85ff9
          # locked
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          e2e33f175e79ff7ff8d44b3176378b5d
          # locked
          """,
          'hidden': False,
          'locked': True,
>>>>>>> 1b2f0006a5630ca26f1637d81bcd190d73b7231d
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
