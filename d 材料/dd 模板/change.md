<%*
const action = await tp.system.prompt("请输入操作类型");
const color = action === "添加" ? "#8CC152" :
              action === "修改" ? "#4A89DC" :
              action === "管理" ? "#967ADC" :
              action === "删除" ? "#E9573F" :
              action === "存档" ? "#FC6E51" :
              "#000000";
const problemNumber = await tp.system.prompt("请输入问题编号");
const today = tp.date.now("YYYY-MM-DD");

tR = `${today}：<font color="${color}">${action}</font> - [[c 题库（伸长版）/Problem ${problemNumber}|${problemNumber}]] - `;
%>