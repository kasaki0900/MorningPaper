import json
d = {
    'title': '现在还不是以色列最危险的时候，最危险的时候在月末',
     'text': '目前战况是哈马斯从加沙前出进攻，以色列处于防守反击状态，而以色列已经开战争动员30万预备役，动员是要时间的，怎么也得一周到两周，根据以色列目前的发言，要围困加沙攻城彻底解决哈马斯。但我们都知道的，动员兵战斗力不会很高，主力还是正规军为主，到时候一旦开始围攻加沙，北部防线将处于脆弱状态，会暴露一个巨大的破绽给黎巴嫩真主党和叙利亚。介时以色列主力军团全围在加沙，真主党南下，而叙利亚收回戈兰高 地，以色列将没有任何后备兵员可用。所以加沙不是大问题，如何防住北面才是大问题。',
     'img': ['http://tiebapic.baidu.com/forum/w%3D580/sign=9252e38423380cd7e61ea2e59144ad14/1b5890ef76c6a7efec37b412bbfaaf51f3de66be.jpg?tbpicau=2023-10-15-05_a3c4c0f74764d61548d40b92e6ead967']
     }

print(json.JSONEncoder(ensure_ascii=False).encode(d))
