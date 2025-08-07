# Maple Neon：Cherry Studio 主题

![Free Palestine](https://freepalestinemovement.org/wp-content/uploads/2013/06/banner.jpg)
![Cherry Studio](https://www.cherry-ai.com/assets/cherry-logo-CtmH594q.svg)
![Static Badge](https://img.shields.io/badge/Tailored_for-Cherry_Studio-red?logo=Github)
![Static Badge](https://img.shields.io/badge/License-MIT-blue)
![Static Badge](https://img.shields.io/badge/Language-SCSS-pink?logo=css)
![Static Badge](https://img.shields.io/badge/Release-v1.2.1-green)
<div style="text-align: center">
中文 |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/README.md">English</a> |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.fr.md">Français</a> |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.ja.md">日本語</a>
</div>

## 介绍

这是一款为Cherry Studio量身定制的主题，Cherry Studio是一款支持多个大语言模型供应商的桌面客户端，可在Windows、Mac和Linux系统上使用。\
如需了解更多关于Cherry Studio的信息，请查看[此处](https://github.com/CherryHQ/cherry-studio)。

## 使用方法

1. （推荐但非必需）下载 [Maple 字体](https://github.com/subframe7536/maple-font/releases/download/v7.3/MapleMono-NF-CN-unhinted.zip)。如果你不喜欢该字体，默认的备用字体应为`Fira Code`。
2. （推荐但非必需）从 [鸿蒙字体](https://developer.huawei.com/images/download/general/HarmonyOS-Sans.zip) 下载鸿蒙字体。如果你不喜欢该字体，默认的备用字体应为您的系统UI默认字体。
3. 复制 [maple-neon.scss](../themes/maple-neon.scss) 文件（原始版本）中的内容，或下载原始文件（用于定制）。
4. 将其粘贴到 Cherry Studio 中。
5. 完成！

<details>
<summary>或从这里复制！</summary>

```scss
/* Maple Neon Theme: Complete Version of Maple Neon */

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
    --content-font: "HarmonyOS Sans", "HarmonyOS Sans SC", "Noto Sans", "Noto Sans SC", Ubuntu, -apple-system,
    BlinkMacSystemFont, "Segoe UI", system-ui, Roboto, Oxygen, Cantarell, "Open Sans", "Helvetica Neue", Arial,
    "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --content-font-weight: normal;

    /* 标题/UI 字体 (对应规范中的 --font-family-serif, 但这里保持无衬线优先) */
    --title-font: "HarmonyOS Sans", "HarmonyOS Sans SC", "Noto Serif", "Noto Serif SC", "Microsoft Sans", -apple-system,
    BlinkMacSystemFont, "Segoe UI", system-ui, Ubuntu, Roboto, Oxygen, Cantarell, "Open Sans", "Helvetica Neue",
    serif, Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --title-font-weight: bold;

    /* 代码字体 (对应规范中的 --code-font-family) */
    --monospace-font: "Maple Mono NF CN", "Cascadia Code", "Fira Code", "Consolas", Menlo, Courier, monospace !important;
    --monospace-font-weight: normal;

    --ui-font-weight: bold; /* 保留UI元素的特定粗细控制 */

    // --input-gradient-opacity: 1;

    //   --box-shadow-message: 0 4px 16px -8px rgba(0, 0, 0, 0.04);
    //   --border-radius-message: 16px;
}

/* --- 浅色模式输入栏文本及光标颜色修复 --- */
body[theme-mode="light"] {
    #inputbar input,
    #inputbar textarea,
    #inputbox,
    .form-control {
        color: var(--color-text) !important; /* 使用规范中定义的浅色模式文本颜色 */
        caret-color: var(--color-text) !important; /* 使用规范中定义的浅色模式文本颜色作为光标颜色 */
    }
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

/* --- 动画应用 --- */
[class^="MessageLineContainer"] {
    /* background: var(--chat-background); */ /* 保持 Maple Neon 原有背景 */
    border-radius: var(--button-border-radius);

    [class^="MessageItem"]:active {
        animation: clickAnimation var(--long-timer) var(--animation);
    }
}

[class^="SettingHelpTextRow"] {
    display: inline-block;
}

[class^="Icon"]:hover,
[class^="ant"]:hover,
[class^="ActionButton"]:hover,
[class^="TopicListItem"]:hover,
[class^="ProviderListItem"]:hover,
[class^="MenuItem"]:hover,
[class^="MenuButton"]:hover,
[class^="EmojiBackground"]:hover {
    border-radius: var(--button-border-radius-hover) !important;
    transition: border-radius var(--short-timer) var(--animation);
}

[class^="IconItem"]:active,
[class^="ant-avatar"]:active,
[class^="ant-btn"]:active,
[class^="ant-segmented-item"]:active,
[class^="anticon"]:active,
[class^="ant-upload"]:active,
[class^="ant-divider"]:active,
[class^="ant-tooltip"]:active,
[class^="ant-message"]:active,
[class^="ActionButton"]:active,
[class^="TopicListItem"]:active,
[class^="ProviderListItem"]:active,
[class^="MenuItem"]:active,
[class^="MenuButton"]:active,
[class^="EmojiBackground"]:active,
[class~="ant-dropdown-menu-item"]:active,
[class~="ant-dropdown-menu-submenu-title"]:active,
[class~="ant-select-selector"]:active,
[class~="ant-select-item"]:active {
    border-radius: var(--button-border-radius-active) !important;
    transition: border-radius var(--short-timer) var(--animation);
    animation: clickAnimation var(--long-timer) var(--animation);
}

/* Adapted to v1.2.8 */
[class^="Menus"] {
    [class^="Icon"]:active {
        border-radius: var(--button-border-radius-active) !important;
        transition: border-radius var(--short-timer) var(--animation);
        animation: clickAnimation var(--long-timer) var(--animation);
    }
}

[class^="Icon"],
[class^="ant"],
[class^="ActionButton"],
[class^="TopicListItem"],
[class^="ProviderListItem"],
[class^="MenuItem"],
[class^="MenuButton"],
[class^="EmojiBackground"] {
    border-radius: var(--button-border-radius) !important;
}

[class^="ant-switch"] {
    border-radius: 100px !important;
}

/* 保持 Maple Neon 原有背景色定义 */
/* body[theme-mode="light"] {
    background-color: var(--background-light-new);
}

body[theme-mode="dark"] {
    background-color: var(--background-dark-new) !important;
} */

/* 保持 Maple Neon 原有 hover 效果 */
/* [theme-mode="light"] .bubble .message-user .message-action-button:hover {
    background-color: var(--button-hover-light) !important;
}

[theme-mode="dark"] .bubble .message-user .message-action-button:hover {
    background-color: var(--button-hover-dark) !important;
} */

[theme-mode="light"] button.ant-btn:hover,
[theme-mode="dark"] button.ant-btn:hover {
    border-radius: var(--button-border-radius) !important; /* pulse.scss 中是 --button-border-radius，保持一致 */
}

/* 保持 Maple Neon 原有 input 背景 */
/* [theme-mode="light"] [class^="ant-input"],
[theme-mode="light"] button.ant-btn-variant-outlined {
    background-color: var(--input-bg-light) !important;
}

[theme-mode="dark"] [class^="ant-input"],
[theme-mode="dark"] button.ant-btn-variant-outlined {
    background-color: var(--input-bg-dark) !important;
} */

[class$="-tabs-content"],
[class$="-tab"],
[id^="content-container"],
[class^="MessageContainer"],
[class^="SettingContent"],
[class^="SettingContainer"],
[class^="SettingGroup"],
[class^="MenuList"],
[class^="ProviderList"],
[class^="Main"],
[class~="message-assistant"] {
    animation: page-popup-right var(--short-timer) var(--animation);
}

[class~="message-user"] {
    animation: page-popup-left var(--short-timer) var(--animation);
}

/* Bug fixes from pulse.scss - 检查是否与 Maple Neon 冲突 */
/* .bubble .message-user .message-action-button:hover {
    background-color: var(--color-background-mute);
} */
/* 保持 Maple Neon 原有 hover 效果，避免潜在冲突 */
```

</details>

## 特别之处？

- 为Cherry Studio提供现代且美观的用户界面。
- 将Maple字体与霓虹风格的输入栏相结合，打造独特且视觉效果出众的使用体验。

## 展示

基于Cherry Studio v1.2.4
![浅色页面](../examples/main-page-light.png)

![深色页面](../examples/main-page-dark.png)

## 自定义

您可以 fork 该项目并修改自己的 Cherry Studio 主题，具体说明请查看 [Cherry Studio 文档](https://docs.cherry-ai.com/personalization-settings/css)。

## 多看一眼

如需查看其他主题，请查阅[多看一眼](../OneMoreGlance.md)

## 灵感来源

### 主题

- Dracula Theme: <https://cherrycss.com>
- Neon Theme: <https://cherry-ai.com/css>

### 字体

- Maple Font: <https://github.com/subframe7536/maple-font>
- HarmonyOS Sans: <https://developer.huawei.com/consumer/cn/design/resource/>

### 工具

- 主题部分是在DeepSeek-0324和Claude-3.7的帮助下构建的。

## LICENSE

本项目遵循 [MIT LICENSE](../LICENSE)。
