clc
clear
%∂¡»Î‘≠ ºÕºœÒ
original=imread('C:\Users\Ruossipha\Desktop\20171211224204956.bmp');

original=im2double(original);
% P11
% L_R = 17.8824;
% L_G = 43.5161;
% L_B = 4.11935;
% M_R = 3.45565;
% M_G = 27.1554;
% M_B = 3.86714;
% S_R = 0.029957;
% S_G = 0.184309;
% S_B = 1.46709;
% U = [L_R, L_G, L_B; M_R, M_G, M_B; S_R, S_G, S_B];

% P14
% red
% U_p = [0.14, 0.86, 0; 0.14, 0.86, 0; 0, 0, 1];
% % green
% U_d = [0.33, 0.67, 0; 0.33, 0.67, 0; -0.02, 0.02, 1];
% % blue
% U_t = [1.03, 0.144, -0.144; 0, 0.859, 0.14; 0, 0.859, 0.14];

% new = [];
% for i = 1 : size(original, 1)
%     for j = 1:size(original, 2)
%         new(i,j,:)=U_t * [original(i,j,1), original(i,j,2), original(i,j,3)]';
%     end
% end

% imshow(new)



% P20
for lamda = 0: 0.1 : 1
    U_ap = [((lamda+0.1628)/(1+0.1628)),((1-lamda)/(1+0.1628)), 0; ((0.1628*(1-lamda))/(1+0.1628)),(((1-lamda)/(1+0.1628))+lamda), 0; 0, 0, 1];
    U_ad = [((lamda+0.4945)/(1+0.4945)),((1-lamda)/(1+0.4945)), 0; ((0.4945*(1-lamda))/(1+0.4945)),(((1-lamda)/(1+0.4945))+lamda), 0; 0, 0, 1];
    U_at = [10.3, 0.144, -0.144; 0, ((lamda+6.136)/(1+6.136)),((1-lamda)/(1+6.136)); 0, ((6.136*(1-lamda))/(1+6.136)),(((1-lamda)/(1+6.136))+lamda)];
    new = [];
    for i = 1 : size(original, 1)
        for j = 1:size(original, 2)
            new(i,j,:)=U_ap * [original(i,j,1), original(i,j,2), original(i,j,3)]';
        end
    end
    imshow(new)
    pause
end
