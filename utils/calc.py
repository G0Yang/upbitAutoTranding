# Moving average
def get_ma(peiod: int, data: list):
    if len(data) < peiod:
        raise "len(data) < peiod"
    ma = []
    for i in range(peiod, len(data) + 1):
        ma.append(sum(data[i - peiod:i]) / peiod)
    return ma


# Moving Average Convergence Divergence
def get_macd():
    pass


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # data.reverse()
    output = get_ma(3, data)
    print(data)
    print(output)
