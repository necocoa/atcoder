Python: v3.4.3

アップデート前のバージョン（Python3.4.3）での注意点
- Pythonの注意点
  - 最大公約数gcd()はmathではなくfractionsモジュール
  - f文字列は使えない
- NumPyの注意点
  - 最大公約数numpy.gcd(), 最小公倍数numpy.lcm()は使えない
- SciPyの注意点
  - 順列の総数scipy.special.perm()は使えない
  - 組み合わせの総数scipy.misc.comb()は使える
  - 最小全域木scipy.sparse.csgraph.minimum_spanning_tree()は使える
  - 連結成分scipy.sparse.csgraph.connected_components()は使える
  - 最短経路scipy.sparse.csgraph.shortest_path()は使える
