class Item:
    def __init__(self, auctionId, title, pictUrl, tkCommonRate, zkPrice, tkCommFee):
        self.auctionId = auctionId
        self.title = title
        self.pictUrl = pictUrl
        self.tkCommonRate = tkCommonRate
        self.zkPrice = zkPrice
        self.tkCommFee = tkCommFee
        # self.couponLink=couponLink

    def set_link(self, clickUrl, taoToken, shortLinkUrl):
        self.clickUrl = clickUrl
        self.taoToken = taoToken
        self.shortLinkUrl = shortLinkUrl

    def __str__(self):
        return '商品名称：%s,商品价格:%s,预计返利：%s,返利淘口令：%s'%(self.title,self.zkPrice,self.tkCommFee,self.taoToken)