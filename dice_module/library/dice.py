#!/usr/bin/python

from ansible.module_utils.basic import *
import random

__author__ = 'ru-rocker'


def roll_dice(data):

    is_error = False
    has_changed = False

    gn = data['guess_number']
    nor = data['number_of_roll']
    flag = "You lose"
    res = []
    counter = 1

    while counter <= nor:
        r = random.randrange(1,7)
        result = {
            "round": counter,
            "dice_output" : r
        }
        res.append(result)

        if r == gn:
            counter = nor + 1
            flag = "You win"
            has_changed = True

        counter += 1

    resp = {
        "your_guess": gn,
        "result": flag,
        "dice_fact": res
    }
    meta = {"status" : "OK", "response" : resp}

    return is_error, has_changed, meta


def main():
    fields = {
        "guess_number": {
            "required": True,
            "type": "int",
            "choices": [1, 2, 3, 4, 5, 6]
        },
        "number_of_roll": {
            "required": False,
            "default" : 1,
            "type": "int",
            "choices": [1, 2, 3]
        },
    }

    module = AnsibleModule(argument_spec=fields)

    is_error, has_changed, result = roll_dice(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error playing dice", meta=result)

if __name__ == '__main__':
    main()
