


def isIp(ip):

    ip_lst = ip.split('.')

    if len(ip_lst) != 4:
        return False

    result = []
    for ip_l in ip_lst:
        result.append(True) if len(ip_l)<4 and len(ip_l)>0 else result.append(False)

    if all(result) != True:
        return False

    num = "0123456789"

    for i,ip_l in enumerate(ip_lst):

        if ip_l in num and int(ip_l) <= 255 and int(ip_l)>=0:

            if i==0 and int(ip_l)==0:
                return False
            else:
                result.append(True)
        else:
            return False

    else:
        return all(result)


    print(result)
    print(ip_lst)



if __name__ == "__main__":

    ip = '12.1.0.0'

    print(isIp(ip))