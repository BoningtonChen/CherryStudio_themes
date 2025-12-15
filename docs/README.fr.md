# Maple Neon : Un thème pour Cherry Studio

![Free Palestine](https://freepalestinemovement.org/wp-content/uploads/2013/06/banner.jpg)
![Cherry Studio](https://www.cherry-ai.com/assets/cherry-logo-CtmH594q.svg)
![Static Badge](https://img.shields.io/badge/Tailored_for-Cherry_Studio-red?logo=Github)
![Static Badge](https://img.shields.io/badge/License-MIT-blue)
![Static Badge](https://img.shields.io/badge/Language-CSS-pink?logo=css)
![Static Badge](https://img.shields.io/badge/Release-v1.2.1-green)
<div style="text-align: center">
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.zh.md">中文</a> |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/README.md">English</a> |
Français |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.ja.md">日本語</a>
</div>

## Introduction

Ceci est un thème conçu pour Cherry Studio, un client de bureau qui prend en charge plusieurs fournisseurs de modèles de langage (LLM) et est disponible sur Windows, Mac et Linux. \
Pour plus d'informations sur Cherry Studio, consultez [ici](https://github.com/CherryHQ/cherry-studio).

## Comment utiliser

1. (Recommandé mais pas obligatoire) Téléchargez Maple Mono NF CN depuis [Maple Font](https://github.com/subframe7536/maple-font/releases/download/v7.3/MapleMono-NF-CN-unhinted.zip). Si vous n'aimez pas cette police, la police de secours par défaut devrait être `Fira Code`.
2. (Recommandé mais pas obligatoire) Téléchargez DreamHan Sans et DreamHan Serif depuis [DreamHan Font](https://github.com/Pal3love/dream-han-cjk/releases). Si vous n'aimez pas cette police, le système utilisera Microsoft YaHei comme police de secours.
3. Copiez le contenu du fichier [maple-neon.css](../themes/maple-neon.css) (pour la version d'origine) ou téléchargez le fichier brut (pour la personnalisation).
4. Collez-le dans Cherry Studio.
5. Et voilà !

<details>
<summary>Ou, si vous ne voulez pas modifier, copiez directement le CSS depuis ici !</summary>

```css
/* Maple Neon Theme Font Minimal: Une version du thème Maple Neon qui spécifie uniquement les polices */

/* 动画定义 */
@keyframes clickAnimation {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0.7; /* 轻微的透明度变化作为点击反馈，增强动画效果 */
    }
    100% {
        opacity: 1;
    }
}

@keyframes page-popup-right {
    from {
        transform: translateX(-2em);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 100%;
    }
}

@keyframes page-popup-left {
    from {
        transform: translateX(2em);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 100%;
    }
}

/* 基础变量定义 */
:root {
    //   --chat-background-assistant: #fff;
    //   --color-border: rgba(120, 120, 120, 0.08) !important;

    /* --- 动画相关变量 --- */
    --animation: cubic-bezier(0.25, 0.1, 0.25, 1); /* 调整为更快的 ease-out */
    --short-timer: 0.15s; /* 缩短时间 */
    --long-timer: 0.3s; /* 缩短时间 */
    --button-border-radius: 12px;
    --button-border-radius-hover: 12px; /* 保持 hover 时圆角不变 */
    --button-border-radius-active: 12px; /* 保持 active 时圆角不变 */

    /* --- 字体规范对齐 --- */
    /* 基础字体 (对应规范中的 --font-family) */
    --content-font: "Microsoft YaHei", "微软雅黑", "DreamHan Serif", "梦源宋体", "Noto Sans", "Noto Sans SC", Ubuntu, -apple-system,
    BlinkMacSystemFont, "Segoe UI", system-ui, Roboto, Oxygen, Cantarell, "Open Sans", "Helvetica Neue", Arial,
    "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --content-font-weight: normal;

    /* 标题/UI 字体 (对应规范中的 --font-family-serif, 但这里保持无衬线优先) */
    --title-font: "Microsoft YaHei", "微软雅黑", "DreamHan Sans", "梦源黑体", "Noto Serif", "Noto Serif SC", "Microsoft Sans", -apple-system,
    BlinkMacSystemFont, "Segoe UI", system-ui, Ubuntu, Roboto, Oxygen, Cantarell, "Open Sans", "Helvetica Neue",
    serif, Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --title-font-weight: bold;

    /* 代码字体 (对应规范中的 --code-font-family) */
    --monospace-font: "Maple Mono", "Maple Mono NF CN", "Cascadia Code", "Fira Code", "Consolas", Menlo, Courier, monospace !important;
    --monospace-font-weight: normal;

    --ui-font-weight: bold; /* 保留UI元素的特定粗细控制 */

    // --input-gradient-opacity: 1;

    //   --box-shadow-message: 0 4px 16px -8px rgba(0, 0, 0, 0.04);
    //   --border-radius-message: 16px;
}

/* 消息容器样式：增加霓虹AI助手效果 */
/* 输入框动画效果 */
@keyframes gradientFlow {
    0% {
        background-position: 0 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0 50%;
    }
}

#inputbar::before {
    content: "";
    position: absolute;
    inset: -2px;
    border-radius: inherit;
    padding: 3px;
    background: linear-gradient(
                    90deg,
                    #ff6a01,
                /* 爱马仕橙，原色：#d65f00 */ #f8c91c,
                /* 那不勒斯黄，原色：#ffb800 */ #8a2be2,
                /* 紫罗兰色，原色：#8a2be2 */ #f8c91c,
                /* #ffb800 */ #ff6901 /* #d65e00 */
    );
    background-size: 200% 200%;
    mask:
            linear-gradient(#000 0 0) content-box,
            linear-gradient(#000 0 0);
    -webkit-mask-composite: destination-out; /* 兼容旧版 WebKit 内核浏览器 */
    mask-composite: exclude;
    animation: gradientFlow 4s linear infinite;
    opacity: 0;
    transition: all 0.4s ease-in-out;
    pointer-events: auto;
}

#inputbar:focus-within::before {
    opacity: 1;
}

/* 字体样式更改 */
/* UI元素使用粗体 */
body,
div:not(.message-content-container),
span:not(.message-content-container span),
h1,
h2,
h3,
h4,
h5,
h6,
header,
nav,
.sidebar,
.menu,
.button,
.tabs,
.navigation,
.header,
.footer,
.title {
    font-family: var(--title-font), sans-serif;
    font-weight: var(--title-font-weight);
}

/* 消息内容和输入区域 */
.message-content-container,
.message-content-container *,
p,
li,
ul,
ol,
.form-control,
#inputbox,
textarea {
    font-family: var(--content-font), sans-serif;
    font-weight: var(--content-font-weight);
}

/* 代码块和内联代码的特殊字体处理 */
pre,
pre *,
code,
.markdown-body pre,
.markdown-body pre *,
.markdown-body code {
    font-family: var(--monospace-font), monospace !important;
    font-weight: var(--monospace-font-weight);
    -webkit-font-feature-settings:
            "liga" 1,
            "calt" 1,
            "ss01" 1,
            "ss02" 1,
            "ss03" 1,
            "zero" 1 !important;
    font-feature-settings:
            "liga" 1,
            "calt" 1,
            "ss01" 1,
            "ss02" 1,
            "ss03" 1,
            "zero" 1 !important;
    text-rendering: optimizeLegibility;
}
```

</details>

## Qu'est-ce qui rend le thème spécial ?

- Il propose une interface utilisateur modernisée et esthétique pour Cherry Studio.
- Il mêle la police Maple à une zone de saisie au style néon, créant une expérience unique et visuellement attractive.
- Utilise la série de polices DreamHan et Microsoft YaHei pour fournir un excellent affichage des polices chinoises.

## Démonstration

Basé sur Cherry Studio v1.2.4
![Page claire](../examples/main-page-light.png)

![Page sombre](../examples/main-page-dark.png)

## Personnalisation

Vous pouvez forker le projet et modifier votre propre thème pour Cherry Studio. Pour les instructions détaillées, consultez [Documentation Cherry Studio](https://docs.cherry-ai.com/personalization-settings/css).

## Un dernier coup d'œil

Pour d'autres thèmes, consultez [Un dernier coup d'œil](../OneMoreGlance.md)

## Inspirations

### Thèmes

- Thème Dracula : <https://cherrycss.com>
- Thème Neon : <https://cherry-ai.com/css>

### Polices

- Maple Font : <https://github.com/subframe7536/maple-font>
- DreamHan Sans : <https://github.com/Pal3love/dream-han-cjk/releases>

### Outils  

- Les Thèmes sont construits partiellement avec l'aide de DeepSeek-0324 & Claude-3.7.

## LICENCE

Le projet suit la [Licence MIT](../LICENSE).