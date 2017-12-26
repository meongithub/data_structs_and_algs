def permute(input):
    permute_helper(input, "")

def permute_helper(input, chosen):

    if input == "":
        print("OUTPUT " + chosen)
        


    else:
        for i in range(0, len(input)):
            # print(i)
            char = input[i]            
            chosen += input[i]
            # print("input before chose", input)
            input = input[:i] + input[i+1:]

            permute_helper(input, chosen)
            # print("input passed " + input)
            # print("chosen passed " + chosen)  

            input = input[:i] + char + input[i:]
            chosen = chosen[:-1]
           
            # print("chosen " + chosen)
            # print("input " + input)

if __name__ == "__main__":    
    permute("ab")
