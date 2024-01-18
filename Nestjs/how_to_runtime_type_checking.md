# ValidationPipe에서 타입 체크가 가능한 이유

- TypeScript에서 JavaScript로 빌드 시 TypeScript고유 문법인 Decorator와 :type 이 사라지게 되는데 어떻게 런타임에서 타입 체크가 가능할까?
- 빌드된 자바스크립트 파일을 보면 metadata로 데코레이터 정보를 저장하고 있는 것을 확인할 수 있다.

```bash
exports.MessagesController = MessagesController;
__decorate([
    (0, common_1.Get)(),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", []),
    __metadata("design:returntype", void 0)
], MessagesController.prototype, "listMessages", null);
__decorate([
    (0, common_1.Post)(),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [create_messages_dto_1.CreateMessages]),
    __metadata("design:returntype", void 0)
], MessagesController.prototype, "createMessage", null);
__decorate([
    (0, common_1.Get)('/:id'),
    __param(0, (0, common_1.Param)('id')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String]),
    __metadata("design:returntype", void 0)
], MessagesController.prototype, "getMessage", null);
exports.MessagesController = MessagesController = __decorate([
    (0, common_1.Controller)('messages')
], MessagesController);
```

- tsconfig.json의 emitDecoratorMetadata, experimentalDecorators를 true로 활성화시켜야 위와 같이 동작한다.