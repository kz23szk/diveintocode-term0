
def pca_scratch(data):
    '''
    自作の主成分分析を行う関数
    n次元から2次元のデータにする。
    引数：元データ　(n次元）行（データ数）列の行列
    返り値：２次元に圧縮されたデータの　2行（データ数）列の行列
    '''
    # データの偏差を求める
    data_deviation = np.array([row - np.mean(row)
                               for row in data.transpose()]).transpose()
    # 分散共分散行列を求める
    cov_array = np.cov(data_deviation.T)
    # cov関数を使わないなら下記のようになる
    # X_bar = np.array([row - np.mean(row) \
    #                   for row in X.transpose()]).transpose()
    # cov_array = np.dot(X_bar.T, X_bar) / (X.shape[0]-1)
    print("スクラッチ分散共分散行列")
    print(cov_array)

    # 上の分散共分散行列を用いて固有値、固有ベクトルを求める
    lam, eigen_vecter = np.linalg.eig(cov_array)
    print("スクラッチ固有値")
    print(lam)
    print("スクラッチ固有ベクトル")
    print(eigen_vecter)

    # np.linalg.eig関数では固有値順にソートされていないため
    # 固有ベクトルを固有値の大きい順にならべかえる
    lam_index = [n for n in range(len(lam))]
    for i in range(len(lam)):
        for j in range(i + 1, len(lam)):
            if lam[i] < lam[j]:
                lam[i], lam[j] = lam[j], lam[i]
                lam_index[i], lam_index[j] = lam_index[j], lam_index[i]

    print("スクラッチ第一主成分の寄与率")
    print(lam[0] / sum(lam))

    # 各データの第一主成分の値を計算
    first_axes = np.dot(eigen_vecter[:, lam_index[0]].T, data.T)
    # 各データの第二主成分の値を計算
    second_axes = np.dot(eigen_vecter[:, lam_index[1]].T, data.T)

    return np.array([first_axes, second_axes])
