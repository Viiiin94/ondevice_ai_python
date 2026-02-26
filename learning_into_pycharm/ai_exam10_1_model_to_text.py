import h5py
import numpy as np

filename = "cnn_mnist_micro_0.973.h5"

with h5py.File(filename, 'r') as f:

    int_conv2d_weights = (f['model_weights']['conv2d']['sequential']['conv2d']['kernel'][:] * 128).astype(int)
    int_conv2d_weights = int_conv2d_weights & 0xFF

    filters = []
    for i in range(5):
        filters.append(np.zeros((3, 4)))

    for k in range(5):
        for i in range(3):
            for j in range(4):
                filters[k][i][j] = int_conv2d_weights[i][j][0][k]
        filters[k] = filters[k].astype(int)
        # print(filters[k])

    for i in range(len(filters)):
        np.savetxt('conv2d_filters_{}.txt'.format(i),
                   filters[i], fmt='%2x', delimiter=' ')

    int_conv2d_bias = (f['model_weights']['conv2d']['sequential']['conv2d']['bias'][:] * 128).astype(int)
    int_conv2d_bias = int_conv2d_bias & 0xFF
    # print(int_conv2d_bias)
    np.savetxt('conv2d_bias.txt', int_conv2d_bias, fmt='%2x', delimiter=' ')

    # (3x3 filter 추출) 두번째 레이어 weights
    int_conv2d_1_weights = (f['model_weights']['conv2d_1']['sequential']['conv2d_1']['kernel'][:] * 128).astype(int)
    int_conv2d_1_weights = int_conv2d_1_weights & 0xFF
    print(int_conv2d_1_weights.shape)
    # 가중치 데이터 구조: [높이(3), 너비(3), 입력채널(5), 필터개수(6)]
    num_input_channels = int_conv2d_1_weights.shape[2]
    num_filters = int_conv2d_1_weights.shape[3]  # 마지막 차원인 6를 가져옴
    for k in range(num_input_channels):
        for l in range(num_filters):
            # filter_data는 이미 3x3 모양이므로 reshape 없이 바로 저장 가능
            conv2d_1_filter_data = int_conv2d_1_weights[:, :, k, l]
            np.savetxt('conv2d_1_filters_{}{}.txt'.format(l,k),
                       conv2d_1_filter_data, fmt='%02x', delimiter=' ')
            print(f"Filter {l,k} saved. Shape: {conv2d_1_filter_data.shape}")

    conv2d_1_bias = (f['model_weights']['conv2d_1']['sequential']['conv2d_1']['bias'][:] * 128).astype(int)
    conv2d_1_bias = conv2d_1_bias & 0xFF
    print(conv2d_1_bias)
    np.savetxt('conv2d_1_bias.txt', conv2d_1_bias, fmt='%2x', delimiter=' ')

    dense_weights = (f['model_weights']['dense']['sequential']['dense']['kernel'][:] * 128).astype(int)
    dense_weights = dense_weights & 0xFF
    print(dense_weights)
    np.savetxt('dense_weights.txt',
                   dense_weights.reshape(294, 16), fmt='%2x', delimiter=' ')

    dense_bias = (f['model_weights']['dense']['sequential']['dense']['bias'][:] * 128).astype(int)
    dense_bias = dense_bias & 0xFF
    print(dense_bias)
    np.savetxt('dense_bias.txt', dense_bias, fmt='%2x', delimiter=' ')

    dense_1_weights = (f['model_weights']['dense_1']['sequential']['dense_1']['kernel'][:] * 128).astype(int)
    dense_1_weights = dense_1_weights & 0xFF
    print(dense_1_weights)
    np.savetxt('dense_1_weights.txt',
                   dense_1_weights.reshape(16, 10), fmt='%2x', delimiter=' ')

    dense_1_bias = (f['model_weights']['dense_1']['sequential']['dense_1']['bias'][:] * 128).astype(int)
    dense_1_bias = dense_1_bias & 0xFF
    print(dense_1_bias)
    np.savetxt('dense_1_bias.txt', dense_1_bias, fmt='%2x', delimiter=' ')

    print(list(f.keys()))

    print(list(f['model_weights']['dense']['sequential']['dense']['kernel']))
    print(list(f['model_weights']['dense']['sequential']['dense']['bias'].shape))
    print(list(f['model_weights']['dense_1']['sequential']['dense_1']['bias'].shape))



