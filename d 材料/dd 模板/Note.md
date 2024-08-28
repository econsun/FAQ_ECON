<%*
const filename = tp.file.title;
const number = parseInt(filename.slice(-4));
const paddedNumber = String(number).padStart(4, '0');
const nextNumber = String(number + 1).padStart(4, '0');
const prevNumber = String(number - 1).padStart(4, '0');

tR += `联系方式：<a href="https://qm.qq.com/q/iA1sKuakak">2629223739 (QQ)</a> <a href="mailto:econsunrq@outlook.com">econsunrq@outlook.com (邮箱)</a>\n\n`;
tR += `[[c 题库（伸长版）/Problem ${nextNumber}|下一题]]，[[c 题库（伸长版）/Problem ${prevNumber}|上一题]]\n\n`;
tR += `[[0 主页|回到主页]]，[[4 操作流水|操作流水]]\n\n`;
tR += `![[1 汇总问题（伸长版）#^${paddedNumber}]]`;
%>