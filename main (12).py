def linearsearchProduct(productlist, targetproduct) :
  indices=[]
  for index, product in enumerate(productlist) :
    if product==targetproduct:
      indices. append(index)
  return indices         
product=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
result=linearsearchProduct(product, target) 
print(result)