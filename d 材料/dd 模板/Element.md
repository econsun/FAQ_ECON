<%*
const number = await tp.system.prompt("Enter a number:");
const paddedNumber = String(number).padStart(4, '0');
const questionMM = String(await tp.system.prompt("Enter the MM:")).padStart(2, '0');
const questionDD = String(await tp.system.prompt("Enter the DD:")).padStart(2, '0');
const today = tp.date.now("YYYY - MM - DD");

tR += `> [!question] ${paddedNumber} | \n> \n> \n> \n`;
tR += `> **知识分类**：\n`;
tR += `> **提问日期**：2024 - ${questionMM} - ${questionDD}\n`;
tR += `> **首次编辑**：${today}\n`;
tR += `^${paddedNumber}`;
%>