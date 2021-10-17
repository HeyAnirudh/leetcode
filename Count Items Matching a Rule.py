items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
count=0

ruleLoc = ["type", "color", "name"].index(ruleKey)
print(sum(1 for pair in items if pair[ruleLoc] == ruleValue))
