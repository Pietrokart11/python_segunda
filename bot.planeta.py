import discord
from discord.ext import commands

# 1. Configuração básica para o bot funcionar
config_permissoes = discord.Intents.default()
config_permissoes.message_content = True
bot = commands.Bot(command_prefix="!", intents=config_permissoes)

# 2. O comando de cálculo de prejuízo
@bot.command()
async def economia(ctx, minutos_banho: int, aparelhos_tomada: int):
    # Variáveis lógicas de custo estimado
    custo_minuto_chuveiro = 0.15
    custo_mensal_aparelho = 5.00
    
    # Cálculos simples
    gasto_chuveiro_ano = minutos_banho * custo_minuto_chuveiro * 365
    gasto_tomada_ano = aparelhos_tomada * custo_mensal_aparelho * 12
    total_prejuizo = gasto_chuveiro_ano + gasto_tomada_ano
    
    # Resposta direta no chat
    await ctx.send(f"Seus hábitos custam cerca de **R$ {total_prejuizo:.2f} por ano**! Esse dinheiro vai para o lixo junto com os recursos do planeta.")

# 3. Inicialização usando o seu token da atividade anterior
bot.run("Token")

