# coding:utf-8
import tensorflow as tf


def _generate_params_for_lstm_cell(x_size, h_size, bias_size):
    """generates parameters for pure lstm implementation."""
    x_w = tf.get_variable('x_weights', x_size)
    h_w = tf.get_variable('h_weights', h_size)
    b = tf.get_variable('biases', bias_size,
                        initializer=tf.constant_initializer(0.0))
    return x_w, h_w, b


with tf.variable_scope('gru_nn'):
    '''LSTM实现'''
    # hps.num_embedding_size:输入向量长度
    # hps.num_lstm_nodes:lstm内部单元个数
    with tf.variable_scope('reset'):
        '''定义重置门'''
        rx, rh, rb = _generate_params_for_lstm_cell(
            x_size=[hps.num_embedding_size, hps.num_lstm_nodes[0]],
            h_size=[hps.num_lstm_nodes[0], hps.num_lstm_nodes[0]],
            bias_size=[1, hps.num_lstm_nodes[0]]
        )
    with tf.variable_scope('update'):
        '''定义更新门'''
    zx, zh, zb = _generate_params_for_lstm_cell(
        x_size=[hps.num_embedding_size, hps.num_lstm_nodes[0]],
        h_size=[hps.num_lstm_nodes[0], hps.num_lstm_nodes[0]],
        bias_size=[1, hps.num_lstm_nodes[0]]
    )
    with tf.variable_scope('memory'):
        '''中间状态'''
    cx, ch, cb = _generate_params_for_lstm_cell(
        x_size=[hps.num_embedding_size, hps.num_lstm_nodes[0]],
        h_size=[hps.num_lstm_nodes[0], hps.num_lstm_nodes[0]],
        bias_size=[1, hps.num_lstm_nodes[0]]
    )
    h = tf.Variable(
        tf.zeros([batch_size, hps.num_lstm_nodes[0]]),
        trainable=False
    )

    for i in range(num_timesteps):
        # [batch_size, 1, embed_size]
        embed_input = embed_inputs[:, i, :]
        embed_input = tf.reshape(embed_input,
                                 [batch_size, hps.num_embedding_size])
        reset_gate = tf.sigmoid(
            tf.matmul(embed_input, rx) + tf.matmul(h, rh) + rb)
        update_gate = tf.sigmoid(
            tf.matmul(embed_input, zx) + tf.matmul(h, zh) + zb)
        mid_state = tf.tanh(
            tf.matmul(embed_input, cx) + tf.matmul(h * reset_gate, ch) + cb)
        h = (1 - update_gate) * h + update_gate * mid_state
    last = h
