#!usr/bin/env python
#-*- coding:utf-8 -*-


from models import LSTM_FC_Model, FFNN_Model, Double_LSTM_Model


def LSTM_FC_pred_dep(X, Y, X_test=None, iters=20000, learning_rate=1e-4, dropout_prob=0.5):
    print("lr:", learning_rate)
    print("dropout:", dropout_prob)
    print("iterations:", iters)
    num_count = Y.shape[0]
    input_shape = X.shape[1]
    print('num_count:', num_count)
    print('input_size:', input_shape)
    model = LSTM_FC_Model(num_input=input_shape, num_hidden=[40], num_output=1)

    Loss = []
    for iter in range(iters + 1):
        loss = model.fit(X, Y, learning_rate, dropout_prob)
        Loss.append(loss)
        if iter % 100 == 0:
            print("iteration: %s, loss: %s" % (iter, loss))

        if iter % 5000 == 0:
            model.save_model_params('checkpoints/LSTM_FC_CKPT_{}'.format(str(iter)))

    print('starting predicting......')
    Y_test = model.predict(X_test)
    print('predicting done!')
    return Y_test


def FFNN_pred_dep(X, Y, X_test=None, iters=20000, learning_rate=1e-4, dropout_prob=0.5):
    print ("lr:", learning_rate)
    print ("dropout:", dropout_prob)
    print ("iterations:", iters)
    num_count = Y.shape[0]
    input_shape = X.shape[1]
    print ('num_count:', num_count)
    print ('input_size:', input_shape)
    model = FFNN_Model(num_input=input_shape, num_hidden=[40], num_output=1)

    Loss = []
    for iter in range(iters + 1):
        loss = model.fit(X, Y, learning_rate, dropout_prob)
        Loss.append(loss)
        if iter % 100 == 0:
            print("iteration: %s, loss: %s" % (iter, loss))

        if iter % 5000 == 0:
            model.save_model_params('checkpoints/FFNN_CKPT_{}'.format(str(iter)))

    print('starting predicting......')
    Y_test = model.predict(X_test)
    print('done!')
    return Y_test


def DoubleLSTM_pred_dep(X, Y, X_test=None, iters=1000, learning_rate=1e-1, dropout_prob=0.5):
    print("lr:", learning_rate)
    print("dropout:", dropout_prob)
    print("iterations:", iters)
    num_count = Y.shape[0]
    input_shape = X.shape[1]
    print('num_count:', num_count)
    print('input_size:', input_shape)
    model = Double_LSTM_Model(num_input=input_shape, num_hidden=[40], num_output=1)

    Loss = []
    for iter in range(iters + 1):
        loss = model.fit(X, Y, learning_rate, dropout_prob)
        Loss.append(loss)
        if iter % 100 == 0:
            print("iteration: %s, loss: %s" % (iter, loss))

        if iter % 5000 == 0:
            model.save_model_params('checkpoints/Double_LSTM_CKPT_{}'.format(str(iter)))

    print('starting predicting......')
    Y_test = model.predict(X_test)
    print('predicting done!')
    return Y_test

