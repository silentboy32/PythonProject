
sub = ["Math","Pysics","Chemistry","Hindi","English"]

subject = [] 
for item in sub:
    Take = int(input(f"Please Enter number of {item} "))
    subject.append(Take)

for i, value in enumerate(subject):
    if value <= 33:
        print(f"Fail in {sub[i]} number {value}")


            
