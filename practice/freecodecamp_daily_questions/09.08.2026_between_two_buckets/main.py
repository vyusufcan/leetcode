# Between Two Buckets (freeCodeCamp)
#
# Given two buckets of paint, each with an RGB color and a fullness level,
# return the mixed RGB color as an array of three integers.
#
# Each bucket is a dictionary with a "color" property (a list of three
# integers [r, g, b]) and a "fullness" property (0-100).
# The mixed color is a weighted average of each channel in the two colors
# based on fullness level, with each channel rounded to the nearest integer.
#
# Example:
# bucket_a = {"color": [255, 0, 0], "fullness": 100}
# bucket_b = {"color": [0, 0, 255], "fullness": 0}
# mix_paint(bucket_a, bucket_b) -> [255, 0, 0]

# R kanalı:
# (100*30 + 100*70) / (30+70)
# = (3000 + 7000) / 100
# = 10000 / 100
# = 100

def mix_paint(bucket_a: dict, bucket_b: dict) -> list:

    mix_list = []
    for x in range(0,3):
        mix_list.append(
            round(
                (
                    (bucket_a["color"][x] * bucket_a["fullness"]) +
                    (bucket_b["color"][x] * bucket_b["fullness"])
                ) / (bucket_a["fullness"] + bucket_b["fullness"])
            )
)

    return mix_list


# Test cases
print(mix_paint({"color": [100, 150, 200], "fullness": 30}, {"color": [100, 150, 200], "fullness": 70}))
print(mix_paint({"color": [255, 0, 0], "fullness": 50}, {"color": [0, 0, 255], "fullness": 50}))
