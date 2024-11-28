from api import decode_data

# 주어진 데이터
ingredients = [
    "\ub2ec\uac40 2\uac1c", "\ubc25 1 \uacf5\uae30", "\ucabd\ud30c 2\uac1c",
    "\uc2dd\uc6a9\uc720 1\ud070\uc220", "\uc18c\uae08 \uc57d\uac04", "\uac04\uc7a5 \uc57d\uac04"
]
instructions = [
"\ub2ec\uac40\uc5d0 \uc6b0\uc720, \uc18c\uae08, \ud6c4\ucd94\ub97c \ub123\uace0 \uc798 \uc11e\ub294\ub2e4.", "\ud32c\uc5d0 \ubc84\ud130\ub97c \ub179\uc774\uace0, \ub2ec\uac40\ubb3c\uc744 \ubd80\uc5b4 \ucc9c\ucc9c\ud788 \uc800\uc5b4\uac00\uba70 \uc775\ud78c\ub2e4.", "\uc644\uc804\ud788 \uc775\ud788\uc9c0 \uc54a\uace0 \uc0b4\uc9dd \ubd80\ub4dc\ub7ec\uc6b4 \uc0c1\ud0dc\ub85c \uc644\uc131\ud55c\ub2e4.", "\ud30c\uc2ac\ub9ac\ub97c \ubfcc\ub824 \uc7a5\uc2dd\ud55c\ub2e4."
]
substitutes = {
    "\ucabd\ud30c": ["\ub300\ud30c"]
}

# 디코딩 실행
decoded_ingredients, decoded_substitutes, decoded_instructions = decode_data(
    ingredients,  substitutes, instructions
)

# 결과 출력
print("디코딩된 ingredients:", decoded_ingredients)
print("디코딩된 instructions:", decoded_instructions)
print("디코딩된 substitutes:", decoded_substitutes)

