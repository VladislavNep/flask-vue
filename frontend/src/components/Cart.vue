<template>
  <div class="container my-5">
      <div class="row">
        <div class="col-lg-12 p-5 bg-white rounded shadow-sm mb-5">

          <!-- Shopping cart table -->
          <div class="table-responsive">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 pr-3 text-uppercase">Продукт</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Валюта</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Цена</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Колличество</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase"></div>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(product, index) in products" :key="index">
                  <th scope="row" class="border-0">
                    <div class="py-2">
                      <strong>{{ product.name }}</strong>
                    </div>
                  </th>
                  <td class="border-0 align-middle"><strong>{{ product.currency }}</strong></td>
                  <td class="border-0 align-middle">
                    <strong>
                      <span v-if="product.currency === 'USD'">$</span>
                      <span v-else-if="product.currency === 'RUB'">₽</span>
                      <span v-else-if="product.currency === 'EUR'">€</span>
                      {{ product.price }}
                    </strong>
                  </td>
                  <td class="border-0 align-middle"><strong>{{ product.quantity }}</strong></td>
                  <td class="border-0 align-middle">
                    <button type="button"
                            class="btn btn-danger btn-sm"
                            @click="onDeleteProduct(product)">
                      Delete
                    </button>
                    <button type="button"
                            class="btn btn-warning btn-sm"
                            v-b-modal.edit-product-modal
                            @click="editProduct(product)">
                      Update
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="mt-3" id="add_product">
            <button type="button"
                    class="btn btn-success btn-sm" v-b-modal.product-modal>Добавить продукт</button>
          </div>
          <!-- End -->
        </div>
      </div>
    <div class="row">
      <div class="col-lg-12 p-5 bg-white rounded shadow-sm mb-5">
          <div class="d-flex">
            <div class="total_price d-flex ">
              <span class="pr-3 align-self-center">USD: <strong>$72</strong></span>
              <span class="pr-3 align-self-center">RUB: <strong>₽72</strong></span>
              <span class="pr-3 align-self-center">EUR: <strong>€72</strong></span>
            </div>
            <button type="button" class="btn btn-success btn-sm ml-auto">Посчитать</button>
          </div>
      </div>
    </div>
    <b-modal ref="addProductModal"
             id="product-modal"
             title="Добавьте новый товар в корзину"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Название:"
                      label-for="form-name-input">
            <b-form-input id="form-name-input"
                          type="text"
                          v-model="addProductForm.name"
                          required
                          placeholder="Название товара">
            </b-form-input>
        </b-form-group>

        <b-form-group id="form-currency-group"
                      label="Валюта:"
                      label-for="form-currency-options">
          <b-form-select v-model="addProductForm.currency"
                         id="form-currency-options"
                         :options="currency_options"
                         required>
          </b-form-select>
        </b-form-group>

        <b-form-group id="form-quantity-group"
                    label="Колличество:"
                    label-for="form-quantity-input">
          <b-form-input id="form-quantity-input"
                        type="number"
                        v-model="addProductForm.quantity"
                        required
                        placeholder="Колличество">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-price-group"
                    label="Цена:"
                    label-for="form-price-input">
          <b-form-input id="form-price-input"
                        type="number"
                        v-model="addProductForm.price"
                        required
                        placeholder="Цена товара">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Добавить</b-button>
        <b-button type="reset" variant="danger">Отменить</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editProductModal"
         id="edit-product-modal"
         title="Обновите товар"
         hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                      label="Название:"
                      label-for="form-name-edit-input">
            <b-form-input id="form-name-edit-input"
                          type="text"
                          v-model="editProductForm.name"
                          required
                          placeholder="Название товара">
            </b-form-input>
        </b-form-group>

        <b-form-group id="form-currency-edit-group"
                      label="Валюта:"
                      label-for="form-currency-edit-options">
          <b-form-select v-model="editProductForm.currency"
                         id="form-currency-edit-options"
                         :options="currency_options"
                         required>
          </b-form-select>
        </b-form-group>

        <b-form-group id="form-quantity-edit-group"
                    label="Колличество:"
                    label-for="form-quantity-edit-input">
          <b-form-input id="form-quantity-edit-input"
                        type="number"
                        v-model="editProductForm.quantity"
                        required
                        placeholder="Колличество">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-price-edit-group"
                    label="Цена:"
                    label-for="form-price-edit-input">
          <b-form-input id="form-price-edit-input"
                        type="number"
                        v-model="editProductForm.price"
                        required
                        placeholder="Цена товара">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Добавить</b-button>
        <b-button type="reset" variant="danger">Отменить</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: [],
      total_prices: [],
      addProductForm: {
        name: '',
        currency: '',
        quantity: '',
        price: '',
      },
      editProductForm: {
        id: '',
        name: '',
        currency: '',
        quantity: '',
        price: '',
      },
      currency_options: [
        { value: 'RUB', text: 'RUB' },
        { value: 'USD', text: 'USD' },
        { value: 'EUR', text: 'EUR' },
      ],
    };
  },

  methods: {
    getProducts() {
      const path = 'http://localhost:5000/api/user/cart';
      axios.get(path)
        .then((res) => {
          this.products = res.data.products;
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.error(error);
        });
    },
    addProduct(payload) {
      const path = 'http://localhost:5000/api/user/cart';
      axios.post(path, payload)
        .then(() => {
          this.getProducts();
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.log(error);
          this.getProducts();
        });
    },
    editProduct(product) {
      this.editProductForm = product;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProductModal.hide();
      const payload = {
        name: this.editProductForm.name,
        quantity: this.editProductForm.quantity,
        price: this.editProductForm.price,
        currency: this.editProductForm.currency,
      };
      this.updateProduct(payload, this.editProductForm.id);
    },
    updateProduct(payload, productID) {
      const path = `http://localhost:5000/api/user/cart/product/${productID}`;
      axios.put(path, payload)
        .then(() => {
          this.getProducts();
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.error(error);
          this.getProducts();
        });
    },
    removeProduct(productID) {
      const path = `http://localhost:5000/api/user/cart/product/${productID}`;
      axios.delete(path)
        .then(() => {
          this.getProducts();
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.error(error);
          this.getProducts();
        });
    },
    onDeleteProduct(product) {
      this.removeProduct(product.id);
    },
    initForm() {
      this.addProductForm.name = '';
      this.addProductForm.quantity = null;
      this.addProductForm.price = null;
      this.addProductForm.currency = null;
      this.editProductForm.id = '';
      this.editProductForm.name = '';
      this.editProductForm.quantity = null;
      this.editProductForm.price = null;
      this.editProductForm.currency = null;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProductModal.hide();
      const payload = {
        name: this.addProductForm.name,
        currency: this.addProductForm.currency,
        price: this.addProductForm.price,
        quantity: this.addProductForm.quantity,
      };
      this.addProduct(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addProductModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProductModal.hide();
      this.initForm();
      this.getProducts();
    },
  },
  created() {
    this.getProducts();
  },
};
</script>

<style>
#add_product{
  padding-left: 12px;
}
</style>
