import json
import server


def results_to_json(results, model):
    return [
        [
            {
                "class": int(pred[5]),
                "class_name": model.model.names[int(pred[5])],
                "normalized_box": pred[:4].tolist(),
                "confidence": float(pred[4]),
            }
            for pred in result
        ]
        for result in results.xyxyn
    ]


def json_to_solitaire(x):
    y = json.loads(x)
    print(y["normalized_box"][0])
    z = json.dumps(y, indent=2)
    print(z)


def main():
    # some JSON:
    x = '{ "class":"5", "class_name":"4d","normalized_box":[2,3,4],"confidence": "0.55"}'
    json_to_solitaire(x)
    server.testxd()


if __name__ == '__main__':
    main()
