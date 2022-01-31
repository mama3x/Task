import json
with open('tests.json', 'r', encoding='utf8') as dict1:
    a_dict=json.load(dict1)
   
with open('values.json', 'r', encoding='utf8') as dict2:
    b_dict=json.load(dict2)

def set_value(d):
    if not isinstance(d, dict):
        return d
    if d.get("value"):
        return d
    r = [x.get("value") for x in b_dict["values"] if x.get("id") == d.get("id")]
    if r and r[0]:
        d["value"] = r[0]
    return d

def apply_recursive(func, obj):
    if isinstance(obj, list):
        return [apply_recursive(func, elem) for elem in obj]
    elif isinstance(obj, dict):
        obj = func(obj)
        return {k: apply_recursive(func, v) for k, v in obj.items()}
    else:
        return func(obj)
        
_ = apply_recursive(set_value, a_dict) 
print(a_dict)