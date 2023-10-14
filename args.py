import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        action='store_true',
        help='Test mode, helping me see are the damn port working.'
    )
    parser.add_argument(
        "--url",
        default='/f?kw=%E8%88%AA%E7%A9%BA%E6%AF%8D%E8%88%B0',
        help='Url of web which you wanna get.'
    )
    parser.add_argument(
        "--head",
        default='https://tieba.baidu.com',
        help='url head'
    )
    parser.add_argument(
        "--host",
        default='http://localhost:5701'
    )
    return parser.parse_args()





