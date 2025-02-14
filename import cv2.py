import cv2

# Carrega duas capturas de tela para comparação
img1 = cv2.imread(r"C:\Users\not\Desktop\diferente.png")
img2 = cv2.imread(r"C:\Users\not\Desktop\igual.png")

# Converte para escala de cinza e calcula diferenças
#diff = cv2.absdiff(cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY))
#if cv2.countNonZero(diff) > 0:
#    print("Diferenças visuais detectadas")
#else:
#    print("Sem diferenças visuais")
# Verificar se as imagens foram carregadas corretamente
# Verificar se as imagens foram carregadas corretamente
if img1 is None or img2 is None:
    print("Erro: Uma ou ambas as imagens não foram carregadas. Verifique os arquivos.")
    exit()

# Definir um tamanho comum baseado na primeira imagem
altura, largura = img1.shape[:2]
img2 = cv2.resize(img2, (largura, altura))

# Converter para escala de cinza
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Comparar as imagens
diff = cv2.absdiff(gray1, gray2)

# Exibir a diferença
cv2.imshow("Diferença", diff)
cv2.imwrite("diferenca.png", diff)
print("Imagem de diferença salva como 'diferenca.png'. Abra-a manualmente.")
cv2.waitKey(0)
cv2.destroyAllWindows()