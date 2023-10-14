import json
import args
import req


def run_script():
    arguments = args.get_args()
    print(arguments.test)
    js = req.html_update((arguments.head, arguments.url), use_cache=arguments.test)
    response = req.requests.post(arguments.host, json=js)

    print("Code =", response)


if __name__ == '__main__':
    run_script()
