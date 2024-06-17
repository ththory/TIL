# module.exports와 exports의 관계

- exports는 module.exports를 call by reference로 바라보고 있다
- exports = new Object()를 해버리면 새로운 객체가 할당되어버리지만
exports.test = new Object()를 하면 module.exports에 test: new Object()가 생긴다
- exports를 사용할 때에는 직접 객체를 할당하지 말자

```
var module = {
	exports: {}
};
var exports = module.exports;

return module.exports;
```