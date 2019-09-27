error = str(input())
sample_input = input()
sample_input = [int(i) for i in sample_input]

if error == 'deletion':
    ## ОШИБКА ВЫПАДЕНИЯ

    n = len(sample_input) + 1

    sum_S_ = 0
    weight_word = 0

    for index, i in enumerate(sample_input):
        if i == 1:
            sum_S_ += index + 1
            weight_word += 1


    sum_S_ = - sum_S_
    S_ = sum_S_ % (n + 1)


    if S_ < weight_word: ## выпавший символ 0
        n_1 = S_ ## Кол-во единиц, стоящих правее выпавшего символа

        sample_input_inverse = sample_input[::-1]

        one = 0
        for index, j in enumerate(sample_input_inverse):
            if j == 1:
                one += 1

                if one == n_1:
                    index_zero = index + 1
                    break

        sample_input_inverse.insert(index_zero, 0)  
        output = sample_input_inverse[::-1]



    elif S_ > weight_word: ## выпавший символ 1
        n_0 = n - S_ ## Кол-во нулей, стоящих правее выпавшего симовла

        sample_input_inverse = sample_input[::-1]

        zeros = 0
        for index, j in enumerate(sample_input_inverse):
            if j == 0:
                zeros += 1

                if zeros == n_0:
                    index_one = index+1
                    break

        sample_input_inverse.insert(index_one, 1)  
        output = sample_input_inverse[::-1]







elif error == 'insertion':
    ## ОШИБКА ВСТАВКИ


    n = len(sample_input) - 1

    sum_S_ = 0
    weight_word = 0

    for index, i in enumerate(sample_input):
        if i == 1:
            sum_S_ += index + 1
            weight_word += 1


    # sum_S_ = - sum_S_
    T = sum_S_ % (n + 1)

    if T == 0:
        output = sample_input[:-1]

    elif T == weight_word and weight_word > 0:
        output = sample_input[1:]

    elif T > 0 and T != weight_word:

        if T < weight_word: ### Лишний символ 0
            n_1 = T

            sample_input_inverse = sample_input[::-1]

            one = 0
            for index, j in enumerate(sample_input_inverse):
                if j == 1:
                    one += 1

                    if one == n_1:
                        index_error = index + 1
                        break

            del sample_input_inverse[index_error]
            output = sample_input_inverse[::-1]

        if T > weight_word: ### Лишний символ 1
            n_0 = n + 1 - T


            sample_input_inverse = sample_input[::-1]

            zeros = 0
            for index, j in enumerate(sample_input_inverse):
                if j == 0:
                    zeros += 1

                    if zeros == n_0:
                        index_error = index + 1
                        break


            del sample_input_inverse[index_error]
            output = sample_input_inverse[::-1]



print(''.join(str(e) for e in output))
                    
