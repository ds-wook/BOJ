# BOJ
## 백준 알고리즘 문제풀이
- Python으로 푸는 알고리즘
- PEP8 기준에 최대한 맞게끔 작성
- 문제풀이 공유

## Python 스타일의 코드 작성
### whitespace

- 한 줄의 문자 길이가 79자 이하여야 한다.
- 함수와 클래스는 빈 줄 두 개로 구분한다.
- 클래스에서 메서드는 빈 줄 하나로 구분한다.
- 변수 할당 앞 뒤에 스페이스를 하나만 사용한다.
- 리스트 인덱스, 함수 호출, 키워드 인수 할당에는 스페이스를 사용하지 않는다.


### naming

- 함수, 변수, 속성 : `lowercase_underscore`
- 보호(protected) 인스턴스 속성 : `_leading_underscore`
- 비공개(private) 인스턴스 속성 : `__double_leading_underscore`
- 클래스와 예외 : `CapitalizeWord`
- 모듈 수준 상수 : ALL_CAPS
- 클래스의 인스턴스 메서드에서는 첫번째 파라미터 (해당 객체 참조)의 이름을 `self`로 지정
- 클래스 메서드에서는 첫번재 파라미터 (해당 클래스 참조)의 이름을 `cls`로 지정


### 표현식과 문장
- `if no a is b` 보다는 `if a is not b` 를 사용
- `if not somelist` 처럼 빈 값은 암시적으로 False가 된다고 가정
- `if somelist` 처럼 값이 있는 리스트는 암시적으로 True가 된다고 가정
- 한 줄로 된 if문, for, while loop, except 복합문을 쓰지 않는다.
- 항상 파일의 맨 위에 import 문을 놓는다.
- 모듈 임포트시에는 항상 모듈의 절대 이름을 사용 `import foo` 대신 `from bar import foo`
- 상대적인 임포트를 해야 한다면 명시적인 구문을 서서 `from . import foo` 라고 한다.
- 임포트 순서 : 표준 라이브러리 모듈 > 서드파티 모듈 > 자신이 만든 모듈 / 각각의 하위 섹션에서는 알파벳 순서
