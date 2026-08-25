## Summary

<!--
請簡述這個 PR 的目的與背景。

請說明：
- 為什麼需要這個修改？
- 解決了什麼問題？
- 希望達成什麼結果？

請避免只寫「更新設定」、「修正問題」等過於籠統的描述。
-->

## Changes

<!--
請列出這個 PR 實際修改的內容。

建議使用條列式，並盡量具體說明：
- 修改了哪些檔案或設定？
- 新增、修改或移除了哪些功能？
- 是否調整 Keymap、Layer、Behavior、Bluetooth、Power Management 等設定？
- 是否影響 Firmware 行為？
-->

-

## Testing

<!--
請說明你如何驗證這次修改。

如果有測試，請提供：
- 測試環境
- 測試方法
- 測試結果

如果是 ZMK / Firmware 相關修改，請盡可能確認：
- GitHub Actions Build 是否成功
- Firmware 是否可以正常產生
- 實際燒錄後是否正常運作
- 相關按鍵、Layer、Behavior 是否正常
- Bluetooth / Sleep / Wake 等功能是否正常（如果有相關修改）

如果無法進行實機測試，請明確說明原因。
-->

## Breaking Changes

<!--
請確認這個 PR 是否會改變現有使用者的操作方式或行為。

如果有 Breaking Change，請明確說明：
- 哪些功能受到影響？
- 使用者需要做什麼調整？
- 是否需要重新燒錄 Firmware？
- 是否需要修改 Keymap 或其他設定？

如果沒有 Breaking Change，請填寫「無」。
-->

## Related Issues

<!--
如果這個 PR 與 Issue、Discussion 或其他 PR 有關，請在此列出。

例如：

- Relates to #123
- Fixes #123
- Closes #123
-->

## Additional Notes

<!--
請提供 Reviewer 需要知道的其他資訊。

例如：
- 已知限制
- 尚未解決的問題
- 需要特別注意的程式碼
- 需要 Reviewer 特別測試的功能
- 為什麼採用目前的實作方式
-->

<details>
<summary>Checklist</summary>

- [ ] 我已確認這個 PR 的目的與修改內容已清楚說明
- [ ] 我已確認程式碼與設定符合專案規範
- [ ] 我已自行 Review 此次變更
- [ ] 我已完成適當的本機測試
- [ ] 我已確認 GitHub Actions / CI 通過
- [ ] 如果涉及 Firmware，我已確認 Firmware 可以正常 Build
- [ ] 如果可以進行實機測試，我已確認實際功能正常
- [ ] 我已確認沒有引入 Breaking Change，或已在上方明確說明
- [ ] 我已確認相關測試已新增或更新（如適用）
- [ ] 我已確認必要的文件已新增或更新（如適用）
- [ ] 我已確認沒有提交不必要的檔案、Debug code 或暫存內容
- [ ] 我已確認變更範圍與 PR 目的相符，沒有混入無關修改
- [ ] 我已確認 Commit Message 符合 Conventional Commits 規範
- [ ] 我已確認沒有洩漏密碼、Token、私密金鑰或其他敏感資訊
- [ ] 我已確認 Reviewer 可以根據 PR 說明理解這次變更

</details>
