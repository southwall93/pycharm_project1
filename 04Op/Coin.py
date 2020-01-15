def CoinSelect():
    a = int(input("교환할 돈은 얼마?: "))
    w500=a//500
    a=a%500

    w100=a//100
    a=a%100

    w50=a//50
    a=a%50

    w10=a//10
    a=a%10

    print("500원: ",w500,"개")
    print("100원: ",w100,"개")
    print("50원: ",w50,"개")
    print("10원: ",w10,"개")
    print("잔돈: ",a,"원")


CoinSelect()
